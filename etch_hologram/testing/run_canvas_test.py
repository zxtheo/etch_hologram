# importing sys
import sys
import pytest
import tkinter as tk
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'G:\My Drive\\random\\etch_hologram\\etch_hologram\\etch_hologram\\app')

def test_application_not_None():
    import application
    app = application.Application()
    assert app is not None

def test_slider_update():
    from application import Application
    app = Application()
    app.rotation_slider.set(1.5)
    assert app.rotation_slider.get() == 1.5
    app.density_slider.set(25)
    assert app.density_slider.get() == 25
    app.x_adjust_slider.set(-250)
    assert app.x_adjust_slider.get() == -250

def test_slider_min_max():
    from application import Application
    app = Application()
    app.rotation_slider.set(-2)
    assert app.rotation_slider.get() == -2
    app.density_slider.set(2)
    assert app.density_slider.get() == 2
    app.x_adjust_slider.set(-500)
    assert app.x_adjust_slider.get() == -500

def test_slider_out_of_range():
    from application import Application
    app = Application()
    app.rotation_slider.set(-3)
    assert app.rotation_slider.get() == -2
    app.density_slider.set(60)
    assert app.density_slider.get() == 50
    app.x_adjust_slider.set(600)
    assert app.x_adjust_slider.get() == 500

def test_slider_initialization():
    from application import Application
    app = Application()
    assert app.rotation_slider.get() == 0
    assert app.density_slider.get() == 2
    assert app.x_adjust_slider.get() == 0

