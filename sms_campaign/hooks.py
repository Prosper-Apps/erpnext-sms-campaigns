from . import __version__ as app_version

app_name = "sms_campaign"
app_title = "Sms Campaign"
app_publisher = "Finesoft Afrika"
app_description = "Send sms through database query"
app_email = "info@finesoftafrika.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sms_campaign/css/sms_campaign.css"
app_include_js = ["sms.bundle.js",]

# include js, css files in header of web template
# web_include_css = "/assets/sms_campaign/css/sms_campaign.css"
# web_include_js = "/assets/sms_campaign/js/sms_campaign.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sms_campaign/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sms_campaign.utils.jinja_methods",
#	"filters": "sms_campaign.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sms_campaign.install.before_install"
# after_install = "sms_campaign.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sms_campaign.uninstall.before_uninstall"
# after_uninstall = "sms_campaign.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sms_campaign.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_update": "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_triggered_on_update_sms",
		"on_update_after_submit": "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_triggered_on_update_sms",
		"on_cancel": "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_triggered_on_cancel_sms",
		"on_submit": "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_triggered_on_submit_sms",
        "after_insert": "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_triggered_after_insert_sms",
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": [
        "sms_campaign.sms_campaign.doctype.sms_campaign.sms_campaign.send_sheduled_sms"
    ]
}

# scheduler_events = {
#	"all": [
#		"sms_campaign.tasks.all"
#	],
#	"daily": [
#		"sms_campaign.tasks.daily"
#	],
#	"hourly": [
#		"sms_campaign.tasks.hourly"
#	],
#	"weekly": [
#		"sms_campaign.tasks.weekly"
#	],
#	"monthly": [
#		"sms_campaign.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "sms_campaign.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sms_campaign.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sms_campaign.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sms_campaign.utils.before_request"]
# after_request = ["sms_campaign.utils.after_request"]

# Job Events
# ----------
# before_job = ["sms_campaign.utils.before_job"]
# after_job = ["sms_campaign.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sms_campaign.auth.validate"
# ]
