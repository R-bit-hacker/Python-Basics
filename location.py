import phonenumbers
from phonenumbers import geocoder
phone_number1= phonenumbers.parse("+923043636690")
phone_number2= phonenumbers.parse("+923090139836")
phone_number3= phonenumbers.parse("+918878586271")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));

#LETS TRACK PHONE NUMBERS
