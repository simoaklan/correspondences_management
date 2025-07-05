from . import __version__ as app_version

app_name = "correspondences_management"
app_title = "Correspondences Management"
app_publisher = ""
app_description = "Manage incoming and outgoing correspondences"
app_email = ""
app_license = "MIT"

fixtures = [
    {"doctype": "Role", "filters": [["name", "in", ["Correspondences User", "Correspondences Manager"]]]},
    {"doctype": "Workflow", "filters": [["document_type", "=", "Correspondence"]]},
    {"doctype": "Notification", "filters": [["document_type", "=", "Correspondence"]]},
    {"doctype": "Client Script", "filters": [["dt", "=", "Correspondence"]]},
    {"doctype": "Report", "filters": [["ref_doctype", "=", "Correspondence"]]},
]
