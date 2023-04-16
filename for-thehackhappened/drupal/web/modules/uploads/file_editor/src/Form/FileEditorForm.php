<?php

namespace Drupal\file_editor\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;

class FileEditorForm extends FormBase
{

  private $path;
  private $content;

  public function __construct($path, $content)
  {
    $this->path = $path;
    $this->content = $content;
  }

  public function getFormId()
  {
    return 'file_editor_form';
  }

  public function buildForm(array $form, FormStateInterface $form_state)
  {
    $form['path'] = [
      '#type' => 'hidden',
      '#value' => $this->path,
    ];
    $form['content'] = [
      '#type' => 'textarea',
      '#title' => $this->t('File Content'),
      '#description' => $this->t('Edit the file content.'),
      '#default_value' => $this->content,
      '#rows' => 20,
    ];

    $form['submit'] = [
      '#type' => 'submit',
      '#value' => $this->t('Save Changes'),
      '#ajax' => [
        'callback' => '::ajaxSave',
        'event' => 'click',
        'progress' => [
          'type' => 'throbber',
          'message' => $this->t('Saving...'),
        ],
      ],
    ];

    return $form;
  }

  public function submitForm(array &$form, FormStateInterface $form_state)
  {
    // Do nothing here, as the form is submitted via AJAX.
  }

  public function ajaxSave(array $form, FormStateInterface $form_state)
  {
    $response = new \Drupal\Core\Ajax\AjaxResponse();
    try {
      $path = $form_state->getValue('path');
      $content = $form_state->getValue('content');

      file_put_contents($path, $content);

      $message = $this->t('File saved successfully.');
      $response->addCommand(new \Drupal\Core\Ajax\AlertCommand($message));
    } catch (\Exception $e) {
      $message = $this->t('Error saving file: @error', ['@error' => $e->getMessage()]);
      $response->addCommand(new \Drupal\Core\Ajax\AlertCommand($message));
    }

    return $response;
  }
}
