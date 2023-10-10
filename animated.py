from manim import *
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        square = Square()  # Create a square
        
        self.play(Create(square))   # show square on screen
        self.play(Transform(square, circle))   # transform square to sircle
        
        self.play(circle.animate.scale(0.5).shift(RIGHT*2))   # animate the circle
    
