<?php

namespace Drupal\file_editor\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;
use Drupal\file\FileInterface;

class FileUploadForm extends FormBase {

  public function getFormId() {
    return 'file_editor_upload_form';
  }

  public function buildForm(array $form, FormStateInterface $form_state) {
    $form['upload_location'] = [
      '#type' => 'textfield',
      '#title' => $this->t('Upload Location'),
      '#description' => $this->t('Enter the path to the directory where the file should be uploaded.'),
      '#required' => TRUE,
    ];

    $form['file'] = [
      '#type' => 'managed_file',
      '#title' => $this->t('File'),
      '#upload_validators' => [
        'file_validate_extensions' => [''],
      ],
      '#upload_location' => '/opt/drupal/web/',
      '#required' => TRUE,
    ];


    $form['submit'] = [
      '#type' => 'submit',
      '#value' => $this->t('Upload File'),
    ];

    return $form;
  }

  public function submitForm(array &$form, FormStateInterface $form_state) {
    $upload_location = rtrim($form_state->getValue('upload_location'), '/');
    $file = $form_state->getValue('file');
    $file = \Drupal\file\Entity\File::load($file[0]);

    if (file_prepare_directory($upload_location, FILE_CREATE_DIRECTORY)) {
      $destination = $upload_location . '/' . $file->getFilename();
      if (file_unmanaged_copy($file->getFileUri(), $destination, FILE_EXISTS_REPLACE)) {
        \Drupal::messenger()->addMessage($this->t('File uploaded successfully to %destination.', ['%destination' => $destination]));
        $file->delete();
      } else {
        \Drupal::messenger()->addError($this->t('Failed to upload the file to %destination.', ['%destination' => $destination]));
      }
    } else {
      \Drupal::messenger()->addError($this->t('Failed to create or access the directory %directory.', ['%directory' => $upload_location]));
    }
  }
}
