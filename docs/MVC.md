## Controllers

Controllers are the class that delegates tasks to Business Logic classes and are mainly composed only of redirecting functions.

### Controller.redirect
`return Controller.redirect('Controller@method', data_dict)`   
Redirects the flow of program to a controller method specified, sending the data dictionary in the parameter to the method as argument.   
You can pass `False` as the sole argument to this function call to stop the application.

### Controller.error
`return Controller.error(code, message)`   
Prints an error code and message passed in this function and stops the application.

### Controller.view
`return Controller.view('ViewClass', data_dict)`   
Shows the view represented by the view class in the argument, passing the data dictionary as parameter.

## Model 
`db_ref` is a variable that tells if the model represents a table in the database. Assign the variable to `True` if you want to use this framework's default database methods.   
`table` variable tells the model what table this model represents.

#### select
`model_obj.select(col_names)`  
Returns fields specified by the argument of all the records in the table of that model.

#### raw_select
`model_obj.raw_select(query_string)`  
Executes the given query in the database.

#### where
`model_obj.where(column_name, conditional, value, connector='AND')`  
Adds a conditional in the query. You must use this before executing `select`, `update`, or `delete`.

#### insert
`model_obj.insert(data_dict)`  
Inserts the data to the database. The keys of the dictionary must be the actual column names in the table.

#### update
`model_obj.update(data_dict)`
Updates the data on the rows that matches the `where` conditionals previously declared.  
**Note**: If there is no `where` conditional, it will update all rows in the database.

#### delete
`model_obj.delete()`  
Deletes row/s on the database that matches the `where` conditionals previously declared.  
**Note**: If there is no `where` conditional, it will delete ALL rows in the database.

#### migrate
`model_obj.migrate(migration_path)`  
Executes the schema in the migration file for this table.

## View
When extending the framework's View method, you should implement these two functions on your class:
* `show`
    * Usage:
        ~~~python
        def show(self, a_data):
            pass  
        ~~~
    * Function:  
        It handles the showing of the view. It is automatically triggered by `Controller.view` method.

* `close`
    * Usage:
        ~~~python
        def close(self):
            pass
        ~~~
    * Function:  
        It handles the closing of the view.

**Note**:  
When responding to button events, you can make use of `Event`'s event handler. You can do it by inserting `lambda : Event.handle('class.method', data_dict)`
into `"command"` of the `TkinterWidget`.