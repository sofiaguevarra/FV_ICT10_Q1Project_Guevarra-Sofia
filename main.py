from pyscript import document
#information seen in the home page, from seatwork#2
store_name = "ꜱᴏꜰɪ'ꜱ ʙᴏᴏᴋꜱ"
owner_name = "Sofia Francesca Guevarra"
year_founded = "Founded: 2025"
business_hours = "Business Hours: Mon-Sat, 9AM - 7PM"
#if elements are used when handling multiple html's while having only one main.py
#I actually had a hard time with this since it kept showing errors so I asked help from CHATGPT(prompt is sent via gdocs)
if document.getElementById("store_name"):
    document.getElementById("store_name").innerHTML = store_name
if document.getElementById("owner_name"):
    document.getElementById("owner_name").innerHTML = f"Owner: {owner_name}"
if document.getElementById("year_founded"):
    document.getElementById("year_founded").innerHTML = year_founded
if document.getElementById("business_hours"):
    document.getElementById("business_hours").innerHTML = business_hours

#These are used in order to get the total sum of our ordered books
prices = {
    "animal_farm": 200,
    "noli_me_tangere": 300,
    "dekada70": 400,
    "math": 200,
    "sci": 300,
    "eng": 400,
    "twilight": 200,
    "cityof_bones": 300,
    "the_giver": 400,
}

def create_order(event=None): 
    if not document.getElementById("output"):
        return

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    total = 0
    items = []

    for book_id, price in prices.items():
        checkbox = document.getElementById(book_id)
        if checkbox and checkbox.checked:
            total += price
            items.append(book_id.replace("_", " ").title())
#This is for the order summary, its the structure of the text
    summary = (
        f"<b>Order for:</b> {name.title()}<br>"
        f"<b>Address:</b> {address}<br>"
        f"<b>Contact:</b> {contact}<br>"
        f"<b>Items:</b> {', '.join(items) if items else 'None'}<br>"
        f"<b>Total:</b> ₱{total}"
    )
#This is also for the order summary, this is for when we display user's order details
    document.getElementById("output").innerHTML = summary
