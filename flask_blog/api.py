import textrazor
textrazor.api_key = "a6fd329c7a2bbb934ac7bbe316c99c4b550ecfd7bc5f1a32385cf850"

client = textrazor.TextRazor()
client.set_classifiers(["tags"])

# question = 'What is the use of the yield keyword in Python? What does it do?'
# response = client.analyze(question)

# for category in response.categories():
# 	print(category.label, category.score)

def api(question):
	response = client.analyze(question)

	return [x.label for x in response.categories()]

