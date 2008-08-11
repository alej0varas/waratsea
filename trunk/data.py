# data for game
# Copyright (C) 2008 Alejandro Varas <alej0varas@gmail.com>
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

naves = {
    'carak': {
        'palos': ('mayor',),
        'timones': ('normal',),
    },
}


## tipos de palos
palos = {
    'mayor': {
        'velas': ('cangreja',)
    },
}


## tipos de vela
velas = {
    'cangreja': {
        'alto': 10,
        'ancho': 5,
##            'formula': '%s * %s / 2'
    },
}

timones = {
    'normal': {
        'largo' : 1,
        'alto' : 3,
        'max' : 15,
    },
}
