# bot_management
bot managment webapp using flask with admin controlled data of bots details with design similar playstore



### Route: /admin_login

**Description:**
This route allows administrators to log in to the admin dashboard.

**HTTP Methods Supported:**
- GET: Render the admin login form.
- POST: Handle form submission for admin login.

**Parameters:**
- None

**Expected Responses:**
- GET: Renders the admin login form HTML template.
- POST: Redirects to the admin dashboard if login is successful, otherwise, displays an error message.

**Usage Examples:**
- GET Request: Navigate to '/admin_login' to access the admin login form.
- POST Request: Submit the form with valid admin credentials to log in.

---

### Route: /add_bot

**Description:**
This route allows administrators to add a new bot to the database.

**HTTP Methods Supported:**
- GET: Render the add bot form.
- POST: Handle form submission to add a new bot.

**Parameters:**
- None

**Expected Responses:**
- GET: Renders the add bot form HTML template.
- POST: Redirects to the admin dashboard after successfully adding the bot. Displays an error message if validation fails.

**Usage Examples:**
- GET Request: Navigate to '/add_bot' to access the form.
- POST Request: Submit the form with bot details to add a new bot.

---

### Route: /edit_bot/<int:bot_id>

**Description:**
This route allows administrators to edit an existing bot's details.

**HTTP Methods Supported:**
- GET: Render the edit bot form.
- POST: Handle form submission to edit a bot.

**Parameters:**
- bot_id (integer): The unique ID of the bot to edit.

**Expected Responses:**
- GET: Renders the edit bot form with pre-filled data.
- POST: Updates the bot's details and redirects to the admin dashboard.

**Usage Examples:**
- GET Request: Navigate to '/edit_bot/<bot_id>' to edit a specific bot.
- POST Request: Submit the form with edited bot details to save changes.

---

### Route: /edit_screenshots/<int:bot_id>

**Description:**
This route allows administrators to edit the screenshots of a bot.

**HTTP Methods Supported:**
- GET: Render the edit screenshots form.
- POST: Handle form submission to edit screenshots.

**Parameters:**
- bot_id (integer): The unique ID of the bot to edit screenshots for.

**Expected Responses:**
- GET: Renders the edit screenshots form.
- POST: Updates bot's screenshot URLs and redirects to the edit screenshots page.

**Usage Examples:**
- GET Request: Navigate to '/edit_screenshots/<bot_id>' to edit screenshots for a specific bot.
- POST Request: Submit the form to update bot's screenshot URLs.

---

### Route: /delete_screenshot

**Description:**
This route allows administrators to delete a screenshot of a bot.

**HTTP Methods Supported:**
- POST: Handle deletion of a screenshot.

**Parameters:**
- bot_id (integer): The unique ID of the bot.
- screenshot_number (integer): The number of the screenshot to delete.

**Expected Responses:**
- POST: Deletes the specified screenshot and redirects to the edit screenshots page.

**Usage Examples:**
- POST Request: Delete a specific screenshot for a bot.

---

### Route: /admin

**Description:**
This is the admin dashboard route that displays bot information and allows administrators to manage bots.

**HTTP Methods Supported:**
- GET: Render the admin dashboard page.

**Parameters:**
- sort_by (string): Sort bots by name or active status (optional).
- search_query (string): Filter bots by name or description (optional).

**Expected Responses:**
- GET: Renders the admin dashboard page with bot information, sorting, and searching functionality.

**Usage Examples:**
- GET Request: Navigate to '/admin' to access the admin dashboard with sorting and searching options.

---

### Route: /delete_bot/<int:bot_id>

**Description:**
This route allows administrators to delete a bot from the database.

**HTTP Methods Supported:**
- GET: Handle the deletion of a bot.

**Parameters:**
- bot_id (integer): The unique ID of the bot to delete.

**Expected Responses:**
- GET: Deletes the specified bot and its associated data (including screenshots) from the database.

**Usage Examples:**
- GET Request: Navigate to '/delete_bot/<bot_id>' to delete a specific bot.

---

### Route: /contact/

**Description:**
This route allows users to submit a contact form with their name, email, phone number, and message.

**HTTP Methods Supported:**
- POST: Handle form submission for contacting.

**Parameters:**
- None

**Expected Responses:**
- POST: Saves the submitted contact information and message in the database.

**Usage Examples:**
- POST Request: Submit the contact form with user details and a message.

---

### Route: /delete_contact/<int:contact_id>

**Description:**
This route allows administrators to delete a contact message from the database.

**HTTP Methods Supported:**
- POST: Handle the deletion of a contact message.

**Parameters:**
- contact_id (integer): The unique ID of the contact message to delete.

**Expected Responses:**
- POST: Deletes the specified contact message from the database.

**Usage Examples:**
- POST Request: Delete a specific contact message.

---

### Route: /mark_as_read/<int:contact_id>

**Description:**
This route allows administrators to mark a contact message as read in the database.

**HTTP Methods Supported:**
- POST: Handle marking a contact message as read.

**Parameters:**
- contact_id (integer): The unique ID of the contact message to mark as read.

**Expected Responses:**
- POST: Marks the specified contact message as read in the database.

**Usage Examples:**
- POST Request: Mark a specific contact message as read.

---

### Route: /view_bot/<int:bot_id>

**Description:**
This route displays detailed information about a specific bot and allows users to view related bots and provide feedback.

**HTTP Methods Supported:**
- GET: Render the bot details page.

**Parameters:**
- bot_id (integer): The unique ID of the bot to view.

**Expected Responses:**
- GET: Renders the bot details page with bot information, related bots, and feedback section.

**Usage Examples:**
- GET Request: Navigate to '/view_bot/<bot_id>' to view details of a specific bot.

---


These are the documentation snippets for the important routes in the Flask application, including both HTML rendering routes and routes that perform actions.
