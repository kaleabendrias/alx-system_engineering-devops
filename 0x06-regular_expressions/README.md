Regular Expression Matching in Ruby
This project involves building a regular expression (regex) in Ruby using the Oniguruma regex library.

Background
Ruby uses Oniguruma regex library by default, which has some different properties than other regex libraries
The focus is on building the regex pattern, the Ruby code is provided
The code takes the regex, applies it to the input argument, and prints matches
Resources
Regular expressions - basics
Regular expressions - advanced
Rubular is an online regex tester for Ruby
RegexOne interactive regex exercises
Requirements
Editors: vi, vim, emacs
Ubuntu 20.04 LTS
Add new line at end of files
README.md file
Executable Bash scripts
Shebang line: #!/usr/bin/env ruby
Use Oniguruma regex library
Code Examples
Match IP address:

ruby

Copy code

#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
Sample usage:

Copy code

$ ./regex_match.rb 127.0.0.2
127.0.0.2
Tasks
Build regex that matches requirement
Test regex thoroughly
Update code with final regex pattern
Handle edge cases
Document code
Useful Resources
Oniguruma Docs
Rubular to test Ruby regex
Let me know if you would like me to explain anything in more detail!
