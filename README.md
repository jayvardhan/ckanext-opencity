# ckanext-opencity

## Installation

To install ckanext-opencity:

1. Activate your CKAN virtual environment, for example:

   source /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

   git clone https://github.com/jayvardhan/ckanext-opencity.git
   cd ckanext-opencity
   pip install -e .
   pip install -r requirements.txt

3. Add `opencity` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

   sudo service apache2 reload

## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.opencity.some_setting = some_default_value

## Developer installation

To install ckanext-opencity for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/jayvardhan/ckanext-opencity.git
    cd ckanext-opencity
    pip install -e .
    pip install -r dev-requirements.txt

