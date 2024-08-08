key_location= "chair"
locations=["sofa", "bedroom", "chair", "garage", "dining"]

for loc in locations:
    if loc==key_location:
        print(f"key found at:{loc} ")
        break
    else:
        print("key not found at: ",loc)

print("END")