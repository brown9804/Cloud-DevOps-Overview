# Working with Text Files and Streams

----------------------
Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/) [brown9804](https://github.com/brown9804)


March, 2022

----------------------

### _Connect to the server_:

`ssh <user_name>@<IPadress>`


## Modify a Text File Using sed:
> Someone got confused and wrote about cows instead of ants in a text file. We've got to replace all instances of cows and with Ants, regardless of whether or not cows contains any capital letters.
### _ See File Content_:
1. Let's look at the file we're dealing with: <br/>
`cat fable.txt`

### _The Fix_:
1. Replace information
> We're going to run a sed command. The -i means "do this in place," as in don't create another file. The capital I near the end stands for "case-insensitive" and means that whether cows has any capital letters in it or not, change it to Ants. The g means do it globally, throughout the whole file.
`sed -i 's/cows/Ants/Ig' fable.txt`
> Now if we run our cat command again, we'll see that all the cows are gone.


## References

https://learn.acloud.guru/course/cad92c58-0fd2-4657-98f7-79268b4ff2db/dashboard
