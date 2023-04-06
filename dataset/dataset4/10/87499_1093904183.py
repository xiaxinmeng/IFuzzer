message = email.message_from_string(
                        # Extract text from xml
                        message_name.find("property_string").text,
                        policy=email.policy.default)