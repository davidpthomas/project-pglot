Project Best Practices
General Guidelines
Code Organization: Organize code into modules and classes to promote reusability and maintainability. Use clear and descriptive names for files and directories.
Documentation: Include module-level docstrings and class/method docstrings to describe the purpose and usage of the code. Use consistent formatting for docstrings.
Error Handling: Use specific exception handling to manage known error scenarios. Log errors with sufficient context to aid in debugging.
Python Code
Class Naming: Use CamelCase for class names. Example:
class QueryNotify:
    ...

Copy

Insert

Apply

Method Naming: Use snake_case for method names. Example:
def start(self, message=None):
    ...

Copy

Insert

Apply

Enum Usage: Use Enum for defining a set of named constants. Example:
class QueryStatus(Enum):
    CLAIMED = "Claimed"
    ...

Copy

Insert

Apply

String Interpolation: Use f-strings for string interpolation for readability and performance. Example:
status += f" ({self.context})"

Copy

Insert

Apply

Imports: Group imports into standard library, third-party, and local imports. Use absolute imports for clarity.
Global Variables: Avoid using global variables. If necessary, clearly document their purpose and usage.
JavaScript/TypeScript Code
Component Naming: Use PascalCase for React component names. Example:
const Label = React.forwardRef(...);

Copy

Insert

Apply

Props and State: Use TypeScript interfaces or types to define component props and state for type safety. Example:
interface Props {
    settings: Settings;
    ...
}

Copy

Insert

Apply

Event Handlers: Prefix event handler methods with handle for clarity. Example:
const handleThemeChange = (theme: EditorTheme) => {
    ...
}

Copy

Insert

Apply

Conditional Rendering: Use short-circuit evaluation for conditional rendering. Example:
{screenRecorderState === ScreenRecorderState.INITIAL && (
    <Button onClick={startScreenRecording}>Record Screen</Button>
)}

Copy

Insert

Apply

CSS-in-JS: Use utility-first CSS frameworks like Tailwind CSS for styling. Apply classes conditionally using helper functions like cn.
Testing
Test Naming: Use descriptive names for test functions to indicate the expected behavior. Example:
def test_interpolate_dict_with_string_values(self):
    ...

Copy

Insert

Apply

Test Coverage: Ensure tests cover various input scenarios, including edge cases and error conditions.
Mocking: Use mocking to isolate the unit under test and avoid dependencies on external systems.
Logging and Debugging
Logging: Use a consistent logging mechanism across the project. Ensure logs provide sufficient context for troubleshooting.
Debugging: Use descriptive error messages and include relevant data in exception handling to facilitate debugging.
Security
Sensitive Data: Avoid hardcoding sensitive information like API keys. Use environment variables or secure vaults.
Input Validation: Validate and sanitize all user inputs to prevent injection attacks.
Version Control
Commit Messages: Use clear and descriptive commit messages. Follow a consistent format, such as "Fix", "Add", "Update", etc.
Branching Strategy: Use a branching strategy that supports the project's workflow, such as Git Flow or GitHub Flow.
Continuous Integration/Continuous Deployment (CI/CD)
Automated Tests: Integrate automated tests into the CI/CD pipeline to ensure code quality and prevent regressions.
Deployment: Use environment-specific configurations for deployments. Automate deployment processes where possible.
Miscellaneous
Environment Configuration: Use .env files for environment-specific configurations. Provide example .env files for developers.
Code Reviews: Conduct regular code reviews to ensure code quality and adherence to best practices. Encourage constructive feedback and knowledge sharing.
