// Desc: Generate invoice for Mo's Lawncare Services
// Author: Victoria Smith
// Dates: Nov 11 2025

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Define program constants.
const BORDER_PERCENT = 0.04;
const BORDER_RATE = 0.28;

const LAWN_PERCENT = 0.95;
const LAWN_RATE = 0.04;

const FERT_RATE = 0.03;

const HST_RATE = 0.15;
const ENV_FEE_RATE = 0.014;

// Start main program here.
// Gather user inputs
let CustName = prompt("Enter the customer name: ");

let StAdd = prompt("Enter the street address: ");
let City = prompt("Enter the city: ");
let PhNum = prompt("Enter the phone number (555-555-5555): ");

let TotSqFt = prompt("Enter the total number of square feet (#####): ");
TotSqFt = parseFloat(TotSqFt);

// Generate program results
let Border = TotSqFt * BORDER_PERCENT;
let BorderCost = Border * BORDER_RATE;

let Lawn = TotSqFt * LAWN_PERCENT;
let LawnCost = Lawn * LAWN_RATE;

let FertCost = TotSqFt * FERT_RATE;

let TotCharges = BorderCost + LawnCost + FertCost;

let HSTCost = TotCharges * HST_RATE;
let EnvFeeCost = TotCharges * ENV_FEE_RATE;

let InvoiceTotal = TotCharges + HSTCost + EnvFeeCost;

// Display results in table formatted invoice
document.writeln("<br />");

document.writeln("<table class='invoicetable'>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2' class='purpbackheadertext'><br />Mo's Lawncare Services - Customer Invoice<br /><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'><br />Customer Details:<br /><br />" +
    "&nbsp;&nbsp;&nbsp;&nbsp;" +
    CustName +
    "<br />" +
    "&nbsp;&nbsp;&nbsp;&nbsp;" +
    StAdd +
    "<br />" +
    "&nbsp;&nbsp;&nbsp;&nbsp;" +
    City +
    "&nbsp;&nbsp;" +
    PhNum +
    "<br /><br />" +
    "Property Size (in sqft): " +
    com2Format.format(TotSqFt) +
    "<br /><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td width='200px'>Border Cost:</td>");
document.writeln(
  "<td class='righttext' width='200px'>" +
    cur2Format.format(BorderCost) +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing Cost:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(LawnCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer Cost:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(FertCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total Charges:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(TotCharges) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales Tax (HST):</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(HSTCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Environmental Cost:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(EnvFeeCost) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice Total:</td>");
document.writeln(
  "<td class='righttext'>" + cur2Format.format(InvoiceTotal) + "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2' class='purpbackfootertext'><br />Turning Lawns into Landscapes<br /><br /></td>"
);
document.writeln("</tr>");

document.writeln("</table>");
