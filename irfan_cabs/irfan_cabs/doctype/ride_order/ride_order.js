// Copyright (c) 2025, Haseeb Ali and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {

    onload(frm){
        console.log ("Running onload");
    },

    setup(frm) {
        console.log("Running setup");
    },

refresh(frm) {
    if (frm.doc.status === "New") {
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Selected");  
                frm.save();
            });
        frm.add_custom_button("Reject", () => {
            frm.set_value("status", "Rejected");
            frm.save();
        });
    } else if (frm.doc.status === "Selected") {
        frm.add_custom_button("Reject", () => {
            frm.set_value("status", "Rejected");
            frm.save();
        });
    } else if (frm.doc.status === "Rejected") {
        frm.add_custom_button("Reset to New", () => {
            frm.set_value("status", "New");
            frm.save();
        });
    }
}
});