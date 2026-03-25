class CareerRecommender:
    def __init__(self):
        pass

    def get_recommendation(self, data):
        coding = data.get("coding")
        problem = data.get("problem")
        security = data.get("security")

        # Decision Logic
        if coding == "yes" and problem == "yes":
            return "Software Developer"

        elif security == "yes":
            return "Cybersecurity Analyst"

        elif coding == "no" and problem == "no":
            return "IT Support Specialist"

        return "General IT / Networking Role"
