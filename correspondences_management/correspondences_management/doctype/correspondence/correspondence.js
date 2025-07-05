frappe.ui.form.on('Correspondence', {
    correspondence_type: function(frm) {
        if (frm.doc.correspondence_type === 'Incoming') {
            frm.set_df_property('department', 'label', 'Receiving Department');
        } else if (frm.doc.correspondence_type === 'Outgoing') {
            frm.set_df_property('department', 'label', 'Sending Department');
        } else {
            frm.set_df_property('department', 'label', 'Department');
        }
    }
});
