// Parent Doctype (Ride Booking)
frappe.ui.form.on('Ride Booking', {
    refresh(frm) {
        calculate_total_amount(frm);
    },
    rate(frm) {
        calculate_total_amount(frm);
    }
});

// Child Table Events (Ride Booking items)
frappe.ui.form.on('Ride Booking items', {
    distance(frm, cdt, cdn) {
        calculate_total_amount(frm);
    },
    items_remove(frm) {
        calculate_total_amount(frm);
    }
});


function calculate_total_amount(frm) {
    let total_distance = 0;
    let rate = frm.doc.rate || 0;

    (frm.doc.items || []).forEach(item => {
        if (item.distance) {
            total_distance += parseFloat(item.distance) || 0;
        }
    });

    const total_amount = rate * total_distance;
    frm.set_value('total_amount', total_amount);
}
