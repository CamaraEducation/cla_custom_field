# To Use:

1. Clone it to your edx-platform directory
2. Install with pip install -e . within this folder within the edx platform virtual environment.
3. Add "custom_reg_form" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
4. Set "REGISTRATION_EXTENSION_FORM" to "custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
5. Run migrations.
6. Start/restart the LMS.

# Or:

1. Login to your edx instance and change to edxapp user, activate edx platform virtual environment and cd into exd-platform folder.
2. With the following command create new app. `./manage.py lms startapp extrainfo`
3. Copy and paste the codes of admin.py, forms.py and models.py files to the newly created app.
4. Add the newly cretaed app and form to your lms.env.json file just like this. `"ADDL_INSTALLED_APPS":["extrainfo"],
"REGISTRATION_EXTENSION_FORM": "extrainfo.forms.ExtraInfoForm",`
5. Run migrations.
6. Start/restart the LMS.