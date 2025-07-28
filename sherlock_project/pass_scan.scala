import scala.io.Source
import scala.util.Using

object PasswordScanner {

  def main(args: Array[String]): Unit = {
    if (args.length != 2) {
      println("Usage: PasswordScanner <passwords_file> <compromised_passwords_file>")
      sys.exit(1)
    }

    val passwordsFile = args(0)
    val compromisedPasswordsFile = args(1)

    val passwords = readLinesFromFile(passwordsFile)
    val compromisedPasswords = readLinesFromFile(compromisedPasswordsFile).toSet

    passwords.foreach { password =>
      if (compromisedPasswords.contains(password)) {
        println(s"Password '$password' is compromised!")
      } else {
        println(s"Password '$password' is safe.")
      }
    }
  }

  def readLinesFromFile(filename: String): List[String] = {
    Using(Source.fromFile(filename)) { source =>
      source.getLines().toList
    }.getOrElse {
      println(s"Error reading file: $filename")
      sys.exit(1)
    }
  }
}