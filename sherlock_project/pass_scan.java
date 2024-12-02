import java.util.Scanner;

/**
* Calculates the strength of a password based on various criteria including length, uppercase letters, lowercase letters, digits, and special characters.
* 
* @param password The password to evaluate its strength.
* @return An integer representing the strength score of the password.
*/
public class PasswordScanner {

    public static int passwordStrength(String password) {
        int score = 0;

        // Check length
        if (password.length() >= 8) {
            score += 1;
        }

        // Check for uppercase letters
        if (password.matches(".*[A-Z].*")) {
            score += 1;
        }

        // Check for lowercase letters
        if (password.matches(".*[a-z].*")) {
            score += 1;
        }

        // Check for digits
        if (password.matches(".*\\d.*")) {
            score += 1;
        }

        // Check for special characters
        if (password.matches(".*[\\W_].*")) {
            score += 1;
        }

        return score;
    }

    public static String evaluatePassword(String password) {
        int score = passwordStrength(password);

        switch (score) {
            case 5:
                return "Very Strong";
            case 4:
                return "Strong";
            case 3:
                return "Moderate";
            case 2:
                return "Weak";
            default:
                return "Very Weak";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a password to evaluate its strength:");
        String password = scanner.nextLine();

        String strength = evaluatePassword(password);
        System.out.println("Password strength: " + strength);
    }
}