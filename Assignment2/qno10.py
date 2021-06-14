st = input("Enter the sentence  : ")
st = st.split(" ")
words = list(reversed(st))
print(" ".join(words))