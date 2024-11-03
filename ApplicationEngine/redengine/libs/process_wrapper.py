import sys, importlib, pickle, pygame, hashlib
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pyredengine import PreviewMain # type: ignore
from functools import partial

class GameHandler():
    def __init__(self, main_file_path: str, project_file_path: str, launch_fullscreen: bool = False) -> None:
        self.main_file_path = main_file_path
        self.project_file_path = project_file_path
        self.process_attached = False
        self.is_fullscreen = launch_fullscreen
        self.hotdump_location = f"{self.project_file_path}/.redengine/hotdump"
        
        self.exclusion_list = [""]
        self.type_exclusions = [pygame.surface.Surface, pygame.Clock, self.__class__]
        
        print("intialised handler succesfulay ")
    
    def start_process(self):  # sourcery skip: class-extract-method
        import importlib.util


        print("Starting Process")
        try:
            print("Before inserting path")
            sys.path.append(self.project_file_path) # Makes the project directory importable
            print(f"Importing Path: {self.project_file_path}")

            try:
                import main  # type: ignore # Import the main project file
                print("Importing File")
            except Exception as e:
                print(f"Error importing main: {e}")

            try:
                importlib.reload(main)  # Reload imports, which will update new code
                print("Reloading Import")
            except Exception as e:
                print(f"Error reloading main: {e}")
        except Exception as e:
            print(f"Error in setup: {e}")

        print("Before Instancing Game")

        self.game: PreviewMain.MainGame = main.Main(self.is_fullscreen) # Instance the game within the handler
        self.game.engine_mode = True
        self.game.__parent = self
        print("After Instancing Game")


        self.process_attached = True

        print("Started Process ")

    def stop_process(self):
        self.game.close_game()
        self.game = None
        self.process_attached = False
        self.is_app_process = False
        
    def hot_reload(self):
        print("started hot reload")

        sys.path.insert(0, self.project_file_path) # Makes the project directory importable
        import main # type: ignore # Import the main project file
        self.save_process_state() # Save the process state 
        
        importlib.reload(main) # Reload imports, which will update new code

        self.game: PreviewMain.MainGame = main.Main(self.is_fullscreen)
        self.load_process_state(self.game)
        
        # self.game.engine_mode = True
        # self.game.__parent = self

        

        print("function finished")
        
    def send_event(self, id, event):
        if type(event) == str and id == "k":
            self.game._send_event(1, event)
        elif type(event) == tuple or type(event) == list and id == "mm":
            self.game._send_event(2, None, [int(event[0]), int(event[1]), int(event[2])])
        if type(event) == tuple or type(event) == list and id == "md":
            self.game._send_event(3, None, [int(event[0]), int(event[1]), int(event[2])])
        elif type(event) == list and id == "mu":
            self.game._send_event(4, None, [int(event[0]), int(event[1]), 0])   

    def run_game(self):
        return self.game.run_game()

    def debug_info(self):
        
        if self.game is None:
            return False
        
        fps = self.game.clock.get_fps()
        delta_time = self.game.get_dt()/1000
        blit_count = self.game.get_total_blits()
        current_tick = self.game.get_tick()
        bps = self.game.get_bps()
        draw_count = self.game.get_draw_calls()
        dps = self.game.get_dps()

        return [delta_time, fps, blit_count, current_tick, bps, draw_count, dps]

    def get_game_process(self):
        return self.game
    
    def get_main_display(self) -> pygame.display: # type: ignore
        return self.game.display
    
    def _get_properties(self):#
        return self.game._obtain_user_vars()
    
    def _get_all_vars(self):
        return {
            attr: getattr(self.game, attr)
            for attr in dir(self.game)
            if not attr.startswith('__')  # Skip dunder methods
            and not callable(getattr(self.game, attr))  # Skip callable attributes
            and attr.startswith('_h_')  # Only get variables that start with '_h_'
            and attr not in self.exclusion_list  # Skip excluded variables
        }

    def _filter_and_serialize_vars(self, vars_dict):
        serialized_vars = {}

        for var_name, value in vars_dict.items():
            # Check if the variable's type is in the exclusion list
            if isinstance(value, tuple(self.type_exclusions)):
                print(f"Skipping serialization for excluded type: {var_name} of type {type(value).__name__}")
                continue

            # Skip serialization if the variable name is in the exclusion list
            if var_name in self.exclusion_list:
                print(f"Skipping serialization for excluded variable: {var_name}")
                continue

            # If it’s a valid variable, serialize it
            serialized_vars[var_name] = value

        return serialized_vars

    def save_process_state(self):
        # Parse the AST of the current file and search for #HOTSAVE commented variables
        hot_saves = self._find_hot_save_variables()
        

        with open(self.hotdump_location, 'wb') as f:
            pickle.dump(hot_saves, f)  # Serialize the hot-saved variables

    def load_process_state(self, game):
        with open(self.hotdump_location, 'rb') as f:
            state = pickle.load(f)  # Load the serialized variables

        for name, value in state[0].items():
            setattr(game, name, value)
            print(f"set {name} to {value}")

        game.on_reload()  # Call a reload function in the game if necessary

    def _find_hot_save_variables(self):  # sourcery skip: low-code-quality
        import ast
        """Parse the current file and find variable assignments with '#HOTSAVE' comment."""
        hot_save_vars = {}
        public_vars = []

        with open(self.main_file_path, "r") as source:
            source_code = source.read()

        tree = ast.parse(source_code)

        for node in ast.walk(tree):
            # Look for attribute assignments (e.g., self._h_angle)
            if isinstance(node, ast.Assign):
                # Find the line number and check for the '#HOTSAVE' comment
                if hasattr(node, 'lineno'):
                    line_num = node.lineno
                    lines = source_code.splitlines()
                    if line_num <= len(lines) and "#[HOTSAVE]" in lines[line_num - 1]:
                        # Handle instance variables like self._h_var
                        for target in node.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                                if target.value.id == "self":  # Detect instance variables
                                    var_name = target.attr
                                    try:
                                        var_value = getattr(self.game, var_name)#eval(compile(ast.Expression(node.value), '<string>', 'eval'))
                                        public_vars.append(var_name)
                                        hot_save_vars[var_name] = var_value
                                        
                                    except Exception as e:
                                        print(f"Error evaluating {var_name}: {e}")
                                        
                    elif line_num <= len(lines) and "#[PUBLIC]" in lines[line_num - 1]:
                        # Handle instance variables like self._h_var
                        for target in node.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                                if target.value.id == "self":  # Detect instance variables
                                    var_name = target.attr
                                    try:
                                        public_vars.append(var_name)
                                    except Exception as e:
                                        print(f"Error evaluating {var_name}: {e}")
        
        
        
        return hot_save_vars, public_vars
   

class Vector3Widget(QWidget):
    stateChanged = pyqtSignal(str, str, str)  # Custom signal to emit when any value changes

    def __init__(self, x=0, y=0, z=0, parent=None):
        super().__init__(parent)

        # Create LineEdits for X, Y, and Z values
        self.line_x = QLineEdit(str(x))
        self.line_y = QLineEdit(str(y))
        self.line_z = QLineEdit(str(z))

        # Create Labels for X, Y, and Z
        self.label_x = QLabel("X:")
        self.label_y = QLabel("Y:")
        self.label_z = QLabel("Z:")

        # Connect text changes to a custom handler
        self.l1_con = self.line_x.editingFinished.connect(self.emit_state_changed)
        self.l2_con = self.line_y.editingFinished.connect(self.emit_state_changed)
        self.l3_con = self.line_z.editingFinished.connect(self.emit_state_changed)

        # Set a layout and add Labels and LineEdits
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean fit

        # Add labels and line edits to the layout
        layout.addWidget(self.label_x)
        layout.addWidget(self.line_x)
        layout.addWidget(self.label_y)
        layout.addWidget(self.line_y)
        layout.addWidget(self.label_z)
        layout.addWidget(self.line_z)

        # Set stretch factors to make all LineEdits fit equally
        layout.setStretch(1, 1)  # Stretch X field
        layout.setStretch(3, 1)  # Stretch Y field
        layout.setStretch(5, 1)  # Stretch Z field

        # Set the layout for this widget
        self.setLayout(layout)

    def emit_state_changed(self):
        # Emit custom signal with current values when any field changes
        self.stateChanged.emit(self.line_x.text(), self.line_y.text(), self.line_z.text())

    def update_value(self, value: tuple):
        self.line_x.setText(str(value[0]))
        self.line_y.setText(str(value[1]))
        self.line_z.setText(str(value[2]))

    def get_val(self):
        return self.line_x.text(), self.line_y.text(), self.line_z.text()

class Color3Widget(Vector3Widget):
    stateChanged = pyqtSignal(pygame.Color)  # Custom signal to emit when any value changes

    def __init__(self, x=0, y=0, z=0, parent=None):
        super().__init__(x=0, y=0, z=0, parent=None)
        
        self.label_x.setText("R: ")
        self.label_y.setText("G: ")
        self.label_z.setText("B: ")
        
        # self.line_x.setValidator(QIntValidator)
        # self.line_y.setValidator(QIntValidator)
        # self.line_z.setValidator(QIntValidator)
        
        
        self.line_x.editingFinished.connect(self.emit_state_changed)
        self.line_y.editingFinished.connect(self.emit_state_changed)
        self.line_z.editingFinished.connect(self.emit_state_changed)
        
        self.line_x.disconnect(self.l1_con)
        self.line_y.disconnect(self.l2_con)
        self.line_z.disconnect(self.l3_con)
        
        
    def emit_state_changed(self):
        # Emit custom signal with current values when any field changes
        self.stateChanged.emit(pygame.Color(int(self.line_x.text()), int(self.line_y.text()), int(self.line_z.text())))

        
    def update_value(self, value: pygame.Color):
        self.line_x.setText(str(value.r))
        self.line_y.setText(str(value.g))
        self.line_z.setText(str(value.b))
        
    def get_val(self):
        return pygame.Color(int(self.line_x.text()), int(self.line_y.text()), int(self.line_z.text()))


class RectWidget(QWidget):
    stateChanged = pyqtSignal(pygame.Rect)  # Custom signal to emit when any value changes

    def __init__(self, rect: pygame.Rect, parent=None):
        super().__init__(parent)

        self.val = rect
        # Create LineEdits for X, Y, and Z values
        self.line_x = QLineEdit(str(rect.left))
        self.line_y = QLineEdit(str(rect.top))
        self.line_z = QLineEdit(str(rect.width))
        self.line_w = QLineEdit(str(rect.height))

        # Create Labels for X, Y, and Z
        self.label_x = QLabel("L:")
        self.label_y = QLabel("T:")
        self.label_z = QLabel("W:")
        self.label_w = QLabel("H:")

        # Connect text changes to a custom handler
        self.line_x.editingFinished.connect(self.emit_state_changed)
        self.line_y.editingFinished.connect(self.emit_state_changed)
        self.line_z.editingFinished.connect(self.emit_state_changed)
        self.line_w.editingFinished.connect(self.emit_state_changed)

        # Set a layout and add Labels and LineEdits
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean fit

        # Add labels and line edits to the layout
        layout.addWidget(self.label_x)
        layout.addWidget(self.line_x)
        layout.addWidget(self.label_y)
        layout.addWidget(self.line_y)
        layout.addWidget(self.label_z)
        layout.addWidget(self.line_z)
        layout.addWidget(self.label_w)
        layout.addWidget(self.line_w)

        # Set stretch factors to make all LineEdits fit equally
        layout.setStretch(1, 1)  # Stretch X field
        layout.setStretch(2, 1)  # Stretch Y field
        layout.setStretch(3, 1)  # Stretch Z field
        layout.setStretch(4, 1)  # Stretch Z field

        # Set the layout for this widget
        self.setLayout(layout)

    def emit_state_changed(self):
        # Emit custom signal with current values when any field changes
        self.stateChanged.emit(pygame.Rect(int(self.line_x.text()), int(self.line_y.text()), int(self.line_z.text()), int(self.line_w.text())))

    def update_value(self, value: pygame.Rect):
        self.val = value
        self.line_x.setText(str(value.left))
        self.line_y.setText(str(value.top))
        self.line_z.setText(str(value.width))
        self.line_w.setText(str(value.height))
        

    def get_val(self):
        return pygame.Rect(int(self.line_x.text()), int(self.line_y.text()), int(self.line_z.text()), int(self.line_w.text()))

class Vector2Widget(QWidget):
    stateChanged = pyqtSignal(str, str)  # Custom signal to emit when any value changes

    def __init__(self, x=0, y=0, parent=None):
        super().__init__(parent)

        # Create LineEdits for X, Y, and Z values
        self.line_x = QLineEdit(str(x))
        self.line_y = QLineEdit(str(y))

        # Create Labels for X, Y, and Z
        self.label_x = QLabel("X:")
        self.label_y = QLabel("Y:")

        # Connect text changes to a custom handler
        self.line_x.editingFinished.connect(self.emit_state_changed)
        self.line_y.editingFinished.connect(self.emit_state_changed)

        # Set a layout and add Labels and LineEdits
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a clean fit

        # Add labels and line edits to the layout
        layout.addWidget(self.label_x)
        layout.addWidget(self.line_x)
        layout.addWidget(self.label_y)
        layout.addWidget(self.line_y)

        # Set stretch factors to make all LineEdits fit equally
        layout.setStretch(1, 1)  # Stretch X field
        layout.setStretch(3, 1)  # Stretch Y field

        # Set the layout for this widget
        self.setLayout(layout)

    def emit_state_changed(self):
        # Emit custom signal with current values when any field changes
        self.stateChanged.emit(self.line_x.text(), self.line_y.text())

    def update_value(self, value: tuple):
        self.line_x.setText(str(value[0]))
        self.line_y.setText(str(value[1]))
        
    def get_val(self):
        return self.line_x.text(), self.line_y.text()
        

     
class PropertiesThread(QThread):
    var_changed = pyqtSignal(int, str)  # Signal to emit index and new value

    def __init__(self, gamehandler, table, timer, pygamewidget, ui, parent=None):
        super().__init__(parent)
        
        self.gamehandler = gamehandler
        self.table: QTableWidget = table
        self.timer: QTimer = timer
        self.running = True
        self.pygame_widget = pygamewidget
        self.ui = ui
   
        self.updating = True

        self.attribute_map = {}  # Map to keep track of attribute to row index
        self.setup_table()  # Setup the initial table

    def setup_table(self):
        
        # Populate the table with variable names and their corresponding values
        if self.ui.properties_options_1.isChecked():
            game_vars = dir(self.gamehandler.game)
        else:
            _, game_vars = self.gamehandler._find_hot_save_variables()
        
        
        built_in_types = (int, float, str, bool, tuple,  list, pygame.Color, pygame.Rect) # Add support for dicts
        blacklist_types = (pygame.Clock)
        user_vars = [var for var in game_vars if not var.startswith("__") and not callable(getattr(self.gamehandler.game, var)) and not isinstance(getattr(self.gamehandler.game, var), blacklist_types)]

        

        self.table.setColumnCount(2)
        self.table.setRowCount(len(user_vars))
        

        # Populate the table and create the attribute map
        for index, att in enumerate(user_vars):
            self.attribute_map[att] = index  # Map the attribute to its row index
            initial_value = getattr(self.gamehandler.game, att)

            tablewidget = QTableWidgetItem(str(att))
            tablewidget.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(index, 0, tablewidget)  # Column 0: Variable name
            tablewidget._initial_value = initial_value

            self.set_cell(index, 1, initial_value, att)

    def set_cell(self, row, col, initial_value, att):
        index = row
        self.table.setRowHeight(index, 28)
                    
        if type(initial_value) == str:
            widget = QLineEdit()
            self.table.setCellWidget(index, 1, widget)
            widget.setText(str(initial_value))

            widget.editingFinished.connect(partial(self.update_var, index, 1, initial_value, att))

        elif type(initial_value) == int:
            widget = QLineEdit()
            self.table.setCellWidget(index, 1, widget)
            widget.setText(str(initial_value))
            widget.setValidator(QIntValidator())

            widget.editingFinished.connect(partial(self.update_var, index, 1, initial_value, att))

        elif type(initial_value) == float:
            widget = QLineEdit()
            self.table.setCellWidget(index, 1, widget)
            widget.setText(str(initial_value))
            widget.setValidator(QDoubleValidator())
            
            

            widget.editingFinished.connect(partial(self.update_var, index, 1, initial_value, att))

        elif type(initial_value) == bool:
            widget = QCheckBox()
            self.table.setCellWidget(index, 1, widget)
            widget.setChecked(initial_value)


            widget.stateChanged.connect(partial(self.update_var, index, 1, initial_value, att))
            
        elif type(initial_value) == tuple:
            if len(initial_value) == 3:
                widget = Vector3Widget(initial_value[0], initial_value[1], initial_value[2])
            elif len(initial_value) == 2:
                widget = Vector2Widget(initial_value[0], initial_value[1])
            
            self.table.setCellWidget(index, 1, widget)
            widget.stateChanged.connect(partial(self.update_var, index, 1, initial_value, att))
        
        elif type(initial_value) == list:
            widget = QTableWidget()
            widget.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            widget._list = initial_value

            widget.setColumnCount(1)
            widget.setRowCount(len(initial_value))
            widget.horizontalHeader().setVisible(False)
            widget.verticalHeader().setVisible(False)
            widget.horizontalHeader().setStretchLastSection(True)
            self.table.setRowHeight(index, 100)
            widget.setGridStyle(Qt.NoPen)
            widget.setAutoFillBackground(True)
            widget.setStyleSheet(u"QTableWidget{ background-color: rgb(25, 25, 25); }")
            
            for c_index, i in enumerate(initial_value):
                child = QTableWidgetItem(str(i))
                widget.setItem(c_index, 0, child) 
            self.table.setCellWidget(index, 1, widget) 

        elif type(initial_value) == pygame.Color:
            widget = Color3Widget(initial_value.r, initial_value.g, initial_value.b)

            self.table.setCellWidget(index, 1, widget)
            widget.stateChanged.connect(partial(self.update_var, index, 1, initial_value, att))
        
        elif type(initial_value) == pygame.Rect:
            widget = RectWidget(initial_value)

            self.table.setCellWidget(index, 1, widget)
            widget.stateChanged.connect(partial(self.update_var, index, 1, initial_value, att))
        else:
            widget = QLabel()
            
            widget.setText(str(initial_value))
            self.table.setCellWidget(index, 1, widget)


    def check_cell(self, row, col, initial_value, att):
        if att is None or initial_value is None or row is None or col is None:
            return None
            
        if initial_value != self.table.item(row, 0)._initial_value:
            if type(initial_value) != type(self.table.item(row, 0)._initial_value):
                return True
            else:
                return False
        else:
            return None                  
            
            
    def run(self):
        if self.pygame_widget.paused:
            return

        try:
            game_vars = dir(self.gamehandler.game)
            built_in_types = (int, float, str, bool, tuple, list, pygame.Color, pygame.Rect)
            user_vars = [var for var in game_vars if not var.startswith("__")]
        except Exception as e:
            return

        prev_values = {}
        prev_types = {}  
        for att in user_vars:
            current_value = getattr(self.gamehandler.game, att)  # Get current value as string
            current_type = type(current_value)

            # If the attribute is new or has changed, emit a signal to update the table
            if att not in prev_values or prev_values[att] != current_value:

                try:
                    if att in self.attribute_map:  # Ensure the attribute is in the map

                        index = self.attribute_map[att]
                        initial_value = current_value

                        check = self.check_cell(index, 1, current_value, att)
                        
                        if check == True:
                        
                            self.table.item(index, 0)._initial_value = initial_value
                            self.set_cell(index, 1, initial_value, att)
   
                        elif check == False:                        
                        
                        

                            if type(initial_value) in [str, int, float]:
                                self.table.cellWidget(index, 1).setText(str(initial_value))  

                            elif type(initial_value) == bool:
                                self.table.cellWidget(index, 1).setChecked(initial_value)
                            
                            elif type(initial_value) == tuple:
                                self.table.cellWidget(index, 1).update_value(initial_value)
                            
                            elif type(initial_value) == list:
                                table: QTableWidget = self.table.cellWidget(index, 1)
                                
                                table.clear()
                                table.setRowCount(len(initial_value))
                                for c_index, i in enumerate(initial_value):
                                    child = QTableWidgetItem(str(i))
                                    table.setItem(c_index, 0, child) 
                                    
                            elif type(initial_value) in [pygame.Rect, pygame.Color]:
                                self.table.cellWidget(index, 1).update_value(initial_value)
                            else:
                                self.table.cellWidget(index, 1).setText(str(initial_value))  



                except Exception as e:
                    print(f"<<Warning>>{e}")
                
            
    def update_var(self, row, col, initial_value, att): 
        print("updating var")
        if self.check_cell(row, col, initial_value, att):
            widget = self.table.cellWidget(row, 1)
            
            if type(initial_value) in [str, int, float]:
                if widget.text() != initial_value:
                    self.update_game_handler(att, widget.text())

            elif type(initial_value) == bool:
                if widget.isChecked() != initial_value:
                    self.update_game_handler(att, widget.isChecked())
            else:
                if widget.get_val() != initial_value:
                    self.update_game_handler(att, widget.get_val())

                            
            
            

     
    def update_game_handler(self, attribute_name, new_value):

        # Assuming all attributes are strings or can be converted to their appropriate types
        try:
            # You may need to convert the new_value to the appropriate type (e.g., int, float)
            # Here we're assuming the attribute can be set as a string
            current_value = getattr(self.gamehandler.game, attribute_name)

            # Convert the new_value to the same type as the current_value
            if isinstance(current_value, int):
                new_value = int(new_value)
            elif isinstance(current_value, float):
                new_value = float(new_value)
            elif isinstance(current_value, bool):
                new_value = new_value.lower() in ['true', '1', 'yes']
            else:
                new_value = new_value

            # Update the game handler's attribute
            setattr(self.gamehandler.game, attribute_name, new_value)



        except Exception as e:
            print(f"Error updating attribute {attribute_name}: {e}")   
     
        

    def stop(self):
        self.running = False  # Method to stop the thread
        self.timer.start(10)