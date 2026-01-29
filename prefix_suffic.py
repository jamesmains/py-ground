text1 = "Mr. Jamesmains"
text2 = "Jamesmains III"

print("[Prefix unmodified]")
print(text1)
print("[Prefix removed]")
print(text1.removeprefix("Mr.").strip())
print("--------------------------------")
print("[Suffix unmodified]")
print(text2)
print("[Suffix removed]")
print(text2.removesuffix("III").strip())
