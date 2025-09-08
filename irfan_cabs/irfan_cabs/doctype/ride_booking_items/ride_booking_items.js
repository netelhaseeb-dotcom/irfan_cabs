// frappe.ui.form.on('Ride Booking items', {
//     distance(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];
//         let rate = frm.doc.rate || 0;

//         // Convert distance to float
//         let new_distance = parseFloat(row.distance) || 0;
//         let old_distance = row._old_distance || 0;

//         // Calculate difference
//         let delta = (new_distance - old_distance) * rate;

//         // Update total amount (in parent)
//         let new_amount = (frm.doc.amount || 0) + delta;
//         frm.set_value('amount', new_amount);

//         // Update the stored distance
//         row._old_distance = new_distance;
//     },

//     // Triggered when a row is loaded
//     items_add(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];
//         row._old_distance = parseFloat(row.distance) || 0;
//     }
// });
