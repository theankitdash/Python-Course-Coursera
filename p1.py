text = "X-DSPAM-Confidence:    0.8475";
text = text.replace(" ", " ")
ind = text.find(":")
print(float(text[ind+1:]))