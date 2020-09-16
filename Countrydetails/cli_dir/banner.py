from .colors import body_colors as bg

class Banner():
    """
    Display the country details banner
    """

    def intro(self):
        """
        Print the banner
        out to the screen
        """
        print("")
        print(("\t\t{} ____                        _                    ____          _              __        ").format(bg.CYLW, bg.CEND))
        print(("\t\t{}(  _ \                      ( )_                 (  _ \        ( )_         _ (_ )       ").format(bg.CYLW, bg.CEND))
        print(("\t\t{}| | (_)  ___   _   _  _____ |  _) ____  _   _    | | | |  ____ |  _)  ____ (_) | |  ____ ").format(bg.CYLW, bg.CEND))
        print(("\t\t{}| |  _  / _ \ | | | |/  _  \| |  (  __)( ) ( )   | | | | / __ \| |   / _  )| | | | /   _)").format(bg.CYLW, bg.CEND)) 
        print(("\t\t{}| |_( )( (_) )| |_| || | | || |  | |   | (_) |   | |_| |(  ___/| |_ ( (_| || | | | \__ \ ").format(bg.CYLW, bg.CEND))
        print(("\t\t{}(____/  \___/  \___/ |_| |_|(__) (_)    \__  |   (____/  \____)\___| \____/|_| (_)(____/").format(bg.CYLW, bg.CEND)) 
        print(("\t\t{}                                       ( )_| |                                          ").format(bg.CYLW, bg.CEND)) 
        print(("\t\t{}                                        \___/                                           ").format(bg.CYLW, bg.CEND)) 
        print("")
        print(("\t\t                                        {} by {}                                         ").format(bg.CCYN,bg.CEND))
        print("")
        print(("\t\t                                 {} ❚█══manumanoj══█❚ {}                                   ").format(
                bg.CGRN,
                bg.CEND,
            ))
        print("")
        print(("\t\t                               {} https://manojmanu.me {}                                ").format(
            bg.CPRP,
            bg.CEND,
        ))
