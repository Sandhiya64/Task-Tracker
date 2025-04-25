from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from task.models import Task
from datetime import datetime
task_bp = Blueprint('tasks', __name__, template_folder='../templates')

@task_bp.route('/')
def index():
    filter_status = request.args.get('status')
    if filter_status == 'completed':
        tasks = Task.query.filter_by(completed=True).all()
    elif filter_status == 'incomplete':
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@task_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form.get('due_date')
        priority = request.form.get('priority')

        task = Task(
            title=title,
            description=description,
            due_date=datetime.strptime(due_date, "%Y-%m-%d") if due_date else None,
            priority=priority
        )
        db.session.add(task)
        db.session.commit()

        flash("Task added successfully!", "success")  # Flash message here
        return redirect(url_for('tasks.index'))
    return render_template('add_task.html')

@task_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        due_date = request.form.get('due_date')
        task.due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        task.priority = request.form.get('priority')

        db.session.commit()

        flash("Task updated successfully!", "success")  # Flash message here
        return redirect(url_for('tasks.index'))

    return render_template('edit_task.html', task=task)


@task_bp.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        task.archived = True # Mark task as completed
        db.session.commit()     # Commit changes to the database
        flash('Task marked as completed!', 'success')  # Success message
    else:
        flash('Task not found.', 'danger')  # If task not found, show error

    return redirect(url_for('tasks.index'))  # Redirect back to the task list


@task_bp.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    flash("Task deleted successfully!", "danger")  # Flash message here
    return redirect(url_for('tasks.index'))

@task_bp.route('/archive/<int:task_id>')
def archive_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.archived = True  # Archive the task
        db.session.commit()
        flash('Task archived!', 'info')
    else:
        flash('Task not found.', 'danger')

    return redirect(url_for('tasks.index'))


