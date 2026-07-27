room_no = int(input("Enter The Room Number:"))

def visit_room(room):
    print("Entered:", room)

    if room==room_no:
        print("Finally found room")
        return
    
    visit_room(room+1)

visit_room(1)