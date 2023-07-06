### Conceptual Exercise

Answer the following questions below:

#### 1. What are important differences between Python and JavaScript?

**Python** _is a general purpose programming language known for its readability and simplicity. It focuses on providing a clear syntax, emphasizing code readability and ease of use._

**JavaScript** _was initially designed as a scripting language for web browsers. It's primary use is for client-side scripting in web development, allowing interactively and dynamic content on web pages._

#### 2. Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") _without_ your programming crashing.

1. **get() method:** _The_ `get()` _method is used to retrieve the value corresponding to the key "c" from the dictionary. If "c" is not present, it returns the specified default value **None** instead of raising a_ `KeyError`. _This approach will allow the program to continue the execution with out crashing._
2. **Use a try-except block:** _With this method the code attempts to access the key directly using square brackets. If the key is not found, a_ `KeyError` _is raised. To handle this exception, the code uses a try-except block. if a_ `KeyError` _occurs, it executes the code within the_ `except` _block, allowing you to handle the missing key._

#### 3. What is a unit test?

**A unit test** _is a type of software testing that focuses on verifying the correctness of individual units or components of a software system. In programming, a unit refers to the smallest testable part of a software application, typically a function, method, or class. Unit tests help identify bugs, validate the logic, and verify the expected outputs of the units being tested._

#### 4. What is an integration test?

**Integration testing** _is to identify issues that arise from combining different components, such as modules, services, or external dependencies, within the system. It ensures that the integrated system functions correctly and that the components work together as expected. By conducting integration tests, developers can ensure the overall correctness, robustness, and smooth functioning of the integrated system as a whole._

#### 5. What is the role of web application framework, like Flask?

**Flask** _is to provide a structured and efficient way to build web applications by handling tasks such as routing, request-response handling, templating, database abstraction, security, and providing an ecosystem of extensions. It simplifies web development, promotes code organization, and improves development efficiency._

#### 6. You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?

**Passing information** _as a parameter in a route URL or using a URL query parameter in Flask depends on the specific needs and requirements of the application. Such as_ `router Parameter` _and_ `URL Query Parameter`.

#### 7. How do you collect data from a URL placeholder parameter using Flask?

**To collect data** _from a URL placeholder parameter using Flask, you can use the route() decorator and specify the parameter name within the route. An Example is:_ `@app.route('/foods/<food_type>')`. _The URL is_ `/foods/pretzel`, _the `food_type` \_parameter within the_ `get_food` _function will be assigned the value_ `'pretzel'` _allowing you to customize the response or perform operations specific to the food type._

#### 8. How do you collect data from the query string using Flask?

**To collect data** _from the query string using Flask, you can access the_ `request.args` _object, which provides a dictionary-like interface to retrieve the values of query parameters._

#### 9. How do you collect data from the body of the request using Flask?

**To collect data** _from the body of a request using Flask, you can access the request.form or_ `request.json` _object, depending on the content type of the request. In Flask, you can collect data from the body of a request by accessing the_ `request.form` _object for form data or the_ `request.json` _object for JSON data._

#### 10. What is a cookie and what kinds of things are they commonly used for?

**A cookie** _is a small data file stored by a web browser on a user's device. They are commonly used for session management, user authentication, and storing user preferences or tracking information._

#### 11. What is the session object in Flask?

**The session object** _in Flask is a feature that enables you to store and retrieve user-specific data across multiple requests. It helps maintain state and store user-related information securely on the server._

#### 12. What does Flask's `jsonify()` do?

**Flask's** `jsonify()` _function serializes Python objects into JSON format and constructs a Flask Response object with the Content-Type header set to "application/json"._
