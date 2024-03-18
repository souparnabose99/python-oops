
# Python variables scopes are defined by the following rule:
# LEGB Rule:
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
print(__name__)

# ----- @TODO Console Output -----


