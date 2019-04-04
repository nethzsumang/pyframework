## Exec Commands

### init
`python exec.py init`  
Initializes the `app.json` contents in the `/config` folder.

### set
`python exec.py set <APP.JSON KEY> <NEW VALUE>`   
Sets a value in `app.json` using the key specified.

### edit_dependency
`python exec.py edit_dependency <package_name> <version>`   
Adds the package name and its required version as a dependency to the application.

### install
`python exec.py install`   
Installs all the dependency packages written in `packages.json`.

### add_support
`python exec.py add_support <support_code>`   
Adds a batch dependency on your application. Supported codes are:
* **image**: adds `opencv-python`, `scikit-image` and `matplotlib` dependencies.
* **ann**: adds `tensorflow` dependency.
* **charts**: adds `matplotlib` dependency.
* **mysql**: adds `mysqlclient` dependency.

### reset_support
`python exec.py reset_support`   
Resets the dependencies to its default values. The default dependencies are:
* `var_dump`: 1.0.0
* `pyquery`: 1.0.0
* `requests`: 1.0.0
* `xlwt`: 1.0.0
* `inflect`: 1.0.0

### generate
`python exec.py generate <file_type> <file_name>`   
Generates a file with the given file type on the default path.   
Available file types are:
* `controller`: Creates to `/app/controllers`.
* `model`: Creates to `app/models`.
* `view`: Creates to `app/views`.
* `event`: Creates to `app/views/events`.

### run
`python exec.py run`   
Runs the application.

### migrate
`python exec.py migrate`   
Adds all the schema JSON files that are in the `database/migrations` folder.