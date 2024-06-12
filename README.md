## Dependencies

> Was written using __Python 3.10.9__

- `pip install PyQt5`
- `pip install PyQt5-stubs`
- `pip install lxml` - _perhaps not needed_

## Progress

### Top Menu "File":
- __Load/Save XML__ - _implemented_
- __Load/Save JSON__ - _implemented_
- __Load/Save SQLite__ - _not implemented_

### Tabs
- __Services__ tab - _implemented_
- __Service Types__ tab - _implemented_
- __Clients__ tab - _implemented_

## Developer's Notes
DryCleaningController -> __active_tab_widget.populate_edit_controls()__ -> (Name)TabWidget -> populate_edit_controls_widget_signal.emit(item, kwargs)

BaseTabWidget -> populate_edit_controls_widget_signal.connect(edit_form_widget.populate_edit_controls)

(Name)EditFormWidget -> populate_edit_controls()