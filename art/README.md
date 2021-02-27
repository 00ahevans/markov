This system is inspired by abstract art and organic shapes. I love bright colors and fun shapes and I'm inspired by many different artists like Picasso and Hilma af Klint. I think art and fashion styles right now are clearly being influenced by the times we are living in. In my opinion, we are seeing more people willing to experiment and take risks in art and fashion because so much of our life is being restricted and put on hold because of COVID. Because of this, people are looking for ways to express themselves in a time where they may not feel seen or heard. I think the color scheme used in my system is representative of this desire to express myself in a creative way.

This system was challenging to me because I had to modify my goals many times. I started this project with the intention of creating an organic shape based on a random starting point and a transition matrix based on the initial point (and previous points). I did a lot of research on how to create organic shapes, and I found two things that looked interesting to me, metaballs and shapes made of bezier curves. I started out trying to use mathematical formulas to generate bezier curves between two points, but this proved very difficult with limited mathematical knowledge. I eventually ended up selecting 28 random shapes using the website blobmaker.app. These shapes were in SVG form, which allowed them to be drawn using the aggdraw module. Although I did not end up generating my own curves, I learned a lot about how organig blob shapes are represented and the methods that computer programs use to make curves. Overall, I really liked how the art turned out, especially the randomly generated coordinates. My next steps going forward would probably be to figure out how to generate a set of points connected by a bezier curve using a transition matrix and markov chains. 

I believe my system aids my own natural creativity, I generated the shapes and colors and this program picks from the shapes and colors I chose to make something original. 




Sources: I used blobmaker.app to generate the SVG blobs that I used to make these drawings. I also used coolors.co to generate a color palette.
I read quite a few stackoverflow articles on using the aggdraw module and how to generate curved shapes, as well as how shapes are represented using an SVG path. Some interesting and helpful posts are linked below.

https://stackoverflow.com/questions/246525/how-can-i-draw-a-bezier-curve-using-pythons-pil/21416678#21416678
https://stackoverflow.com/questions/50731785/create-random-shape-contour-using-matplotlib