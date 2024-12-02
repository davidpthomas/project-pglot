def password_strength(password)
  # Initialize score
  score = 0

  # Check length
  score += 1 if password.length >= 8

  # Check for uppercase letters
  score += 1 if password =~ /[A-Z]/

  # Check for lowercase letters
  score += 1 if password =~ /[a-z]/

  # Check for digits
  score += 1 if password =~ /\d/

  # Check for special characters
  score += 1 if password =~ /[\W_]/

  score
end

def evaluate_password(password)
  score = password_strength(password)

  case score
  when 5
    "Very Strong"
  when 4
    "Strong"
  when 3
    "Moderate"
  when 2
    "Weak"
  else
    "Very Weak"
  end
end

def main
  puts "Enter a password to evaluate its strength:"
  password = gets.chomp

  strength = evaluate_password(password)
  puts "Password strength: #{strength}"
end

main