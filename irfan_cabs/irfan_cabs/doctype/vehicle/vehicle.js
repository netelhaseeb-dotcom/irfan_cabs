// Copyright (c) 2025, Haseeb Ali

frappe.ui.form.on("Vehicle", {
    refresh(frm) {
        // Auto-calculate insurance expiry based on Make
        if (frm.doc.make) {
            const makeYear = parseInt(frm.doc.make);
            const expiryDate = frappe.datetime.obj_to_str(new Date(makeYear + 2, 9, 15)); // Oct 15, make + 2
            frm.set_value("insurance_expiry", expiryDate);

            // Check age warning
            const currentYear = new Date().getFullYear();
            const yearsOld = currentYear - makeYear;

            if (yearsOld >= 2) {
                frappe.msgprint(`This vehicle is ${yearsOld} years old. Your Insurance will be expired !`);
            }

            // Optional: set years of make field
            frm.set_value("years_of_making", yearsOld);
        }
    },

    get_summary(frm) {
        frm.get_field("summary").$wrapper.html("<h1>Hello, here is your Vehicle summary </h1>");
    }
});
