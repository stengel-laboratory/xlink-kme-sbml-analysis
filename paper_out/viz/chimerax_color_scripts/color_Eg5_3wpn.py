from chimerax.core.commands import run
run(session, "close")
session.logger.status("Hello Hello, someone out there???")
run(session, "open 3wpn")
run(session, "color #1:lys hsl(100, 0.5, 0.5)")
run(session, "distance style decimalPlaces 1")
run(session, "distance style dashes 0")
run(session, "distance style radius 0.5")
run(session, "style #1:lys@ca sphere")
run(session, "hide #1:lys@ca cartoon")
run(session, "show #1:lys@ca atom")
run(session, "size atomRadius 2")
run(session, "color  #1/A:146 hsl(0, 0.2, 0.5)")
run(session, "color  #1/A:15 hsl(0, 0.28, 0.5)")
run(session, "color  #1/A:157 hsl(0, 0.23, 0.5)")
run(session, "color  #1/A:17 hsl(0, 0.22, 0.5)")
run(session, "color  #1/A:191 hsl(0, 0.22, 0.5)")
run(session, "color  #1/A:197 hsl(0, 0.22, 0.5)")
run(session, "color  #1/A:207 hsl(0, 0.52, 0.5)")
run(session, "color  #1/A:216 hsl(0, 0.29, 0.5)")
run(session, "color  #1/A:220 hsl(0, 0.29, 0.5)")
run(session, "color  #1/A:246 hsl(0, 0.22, 0.5)")
run(session, "color  #1/A:257 hsl(0, 0.25, 0.5)")
run(session, "color  #1/A:260 hsl(0, 0.23, 0.5)")
run(session, "color  #1/A:315 hsl(0, 0.49, 0.5)")
run(session, "color  #1/A:34 hsl(0, 1.0, 0.5)")
run(session, "color  #1/A:362 hsl(0, 0.25, 0.5)")
run(session, "color  #1/A:368 hsl(0, 0.21, 0.5)")
run(session, "color  #1/A:48 hsl(0, 0.22, 0.5)")
run(session, "color  #1/A:60 hsl(0, 0.23, 0.5)")
run(session, "color  #1/A:64 hsl(0, 0.26, 0.5)")
run(session, "color  #1/A:77 hsl(0, 0.5, 0.5)")
run(session, "distance #1/A:15@CA #1/A:17@CA color hsl(0, 0.41, 0.5)")
run(session, "distance #1/A:15@CA #1/A:191@CA color hsl(0, 0.27, 0.5)")
run(session, "distance #1/A:15@CA #1/A:357@CA color hsl(0, 0.5, 0.5)")
run(session, "distance #1/A:17@CA #1/A:48@CA color hsl(0, 0.49, 0.5)")
run(session, "distance #1/A:17@CA #1/A:357@CA color hsl(0, 0.3, 0.5)")
run(session, "distance #1/A:17@CA #1/A:362@CA color hsl(0, 0.33, 0.5)")
run(session, "distance #1/A:48@CA #1/A:77@CA color hsl(0, 0.51, 0.5)")
run(session, "distance #1/A:48@CA #1/A:357@CA color hsl(0, 0.44, 0.5)")
run(session, "distance #1/A:60@CA #1/A:64@CA color hsl(0, 0.81, 0.5)")
run(session, "distance #1/A:64@CA #1/A:357@CA color hsl(0, 0.35, 0.5)")
run(session, "distance #1/A:77@CA #1/A:207@CA color hsl(0, 0.29, 0.5)")
run(session, "distance #1/A:146@CA #1/A:207@CA color hsl(0, 0.5, 0.5)")
run(session, "distance #1/A:146@CA #1/A:246@CA color hsl(0, 0.35, 0.5)")
run(session, "distance #1/A:146@CA #1/A:257@CA color hsl(0, 0.73, 0.5)")
run(session, "distance #1/A:157@CA #1/A:197@CA color hsl(0, 0.41, 0.5)")
run(session, "distance #1/A:157@CA #1/A:246@CA color hsl(0, 0.43, 0.5)")
run(session, "distance #1/A:157@CA #1/A:260@CA color hsl(0, 0.31, 0.5)")
run(session, "distance #1/A:157@CA #1/A:368@CA color hsl(0, 0.22, 0.5)")
run(session, "distance #1/A:191@CA #1/A:260@CA color hsl(0, 0.35, 0.5)")
run(session, "distance #1/A:191@CA #1/A:315@CA color hsl(0, 0.29, 0.5)")
run(session, "distance #1/A:191@CA #1/A:362@CA color hsl(0, 0.54, 0.5)")
run(session, "distance #1/A:191@CA #1/A:368@CA color hsl(0, 0.28, 0.5)")
run(session, "distance #1/A:197@CA #1/A:220@CA color hsl(0, 0.2, 0.5)")
run(session, "distance #1/A:197@CA #1/A:260@CA color hsl(0, 0.38, 0.5)")
run(session, "distance #1/A:207@CA #1/A:216@CA color hsl(0, 0.26, 0.5)")
run(session, "distance #1/A:216@CA #1/A:220@CA color hsl(0, 0.96, 0.5)")
run(session, "distance #1/A:246@CA #1/A:257@CA color hsl(0, 0.2, 0.5)")
run(session, "distance #1/A:246@CA #1/A:368@CA color hsl(0, 0.41, 0.5)")
run(session, "distance #1/A:257@CA #1/A:368@CA color hsl(0, 0.29, 0.5)")
run(session, "distance #1/A:260@CA #1/A:368@CA color hsl(0, 0.39, 0.5)")
run(session, "distance #1/A:362@CA #1/A:368@CA color hsl(0, 0.22, 0.5)")
