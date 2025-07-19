# login.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, session

voti_bp = Blueprint('voti', __name__)

@voti_bp.route('/', methods=['GET', 'POST'])
def voti():

    return