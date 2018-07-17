
# Catalog App +

This project demonstrates CRUD functionality in web app using Flask and SqlAlchemy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Programming Language:

[Python](https://www.python.org/) - Tested on ver. 3.5.2

#### Virtual Machine

Fork this repository.

On terminal, `cd vagrant/catalog`

Initialize the virtual machine by `vagrant up` then `vagrant ssh`


## Running the Script

After completing the prerequisites above, `cd \vagrant`

run `python loadItems.py` to load sample data to the database

run `python application.py`

## Testing the Web App

On a browser, go to `http://localhost:5000` and test drive the app.

To test the sample json endpoints, enter these url on a browser:

`http://localhost:5000/category/JSON`
`http://localhost:5000/category/<int:category_id>/items/JSON`
`http://localhost:5000/category/<int:category_id>/item/<int:item_id>/JSON`


## Contributing

Please fork this forked repo, and make a PR.


## Note


## Acknowledgements

Udacity and to the original owners the vagrant codes at: https://github.com/udacity/fullstack-nanodegree-vm
