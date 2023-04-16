<?php

namespace Drupal\sql_executor\Form;

use Drupal\Core\Form\FormBase;
use Drupal\Core\Form\FormStateInterface;
use Drupal\Core\Database\Database;
use Symfony\Component\HttpFoundation\Response;

class SQLExecutorForm extends FormBase
{

  public function getFormId()
  {
    return 'sql_executor_form';
  }

  public function buildForm(array $form, FormStateInterface $form_state)
  {
    $form['sql_query'] = [
      '#type' => 'textarea',
      '#title' => $this->t('SQL Query'),
      '#description' => $this->t('Enter an SQL query to execute.'),
      '#required' => TRUE,
    ];

    $form['submit'] = [
      '#type' => 'submit',
      '#value' => $this->t('Execute Query'),
    ];

    return $form;
  }

  public function submitForm(array &$form, FormStateInterface $form_state)
  {
    $query = $form_state->getValue('sql_query');
    $database = Database::getConnection();
    $result = $database->query($query)->fetchAll();
    $response = new Response();
    $response->setContent(json_encode($result));
    $response->headers->set('Content-Type', 'application/json');
    $response->send();
  }
}
