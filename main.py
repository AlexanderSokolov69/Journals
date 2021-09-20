from flask import Flask, render_template, redirect, session, make_response, jsonify, flash, request
from data import db_session, items_api


def main():
    db_session.global_init("db/database.db")
    app.register_blueprint(items_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
