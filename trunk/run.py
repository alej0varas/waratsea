#!/usr/bin/python
# run the game
#Copyright (C) 2008 Alejandro Varas <alej0varas@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor Boston, MA 02110,  USA
# or see <http://www.gnu.org/licenses/>

from juego import Juego

def show_license():
    text = """
        waratsea  Copyright (C) 2008  Alejandro Varas
        This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `show c' for details.
    """
    print text


if __name__  == '__main__':
    show_license()
    juego = Juego()
    juego.main()
