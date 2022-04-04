from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_tokem, get_jwt_identity, jwt_required
from flask_cors import CORS
import models import db