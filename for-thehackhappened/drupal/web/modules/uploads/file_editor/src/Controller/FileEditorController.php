<?php

namespace Drupal\file_editor\Controller;

use Drupal\Core\Controller\ControllerBase;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class FileEditorController extends ControllerBase
{

  public function index(Request $request)
  {
    $filepath = $request->query->get('path', DRUPAL_ROOT);

    if (!is_readable($filepath) || !is_writable($filepath)) {
      return new Response('The file is not readable or writable.', 403);
    }

    if (is_dir($filepath)) {
      return $this->renderDirectory($filepath);
    } else {
      return $this->renderFile($filepath);
    }
  }

  public function save(Request $request)
  {
    $filepath = $request->request->get('path');
    $content = $request->request->get('content');

    if (!is_writable($filepath)) {
      return new Response('The file is not writable.', 403);
    }

    file_put_contents($filepath, $content);
    return new Response('File saved successfully.');
  }

  private function renderDirectory($path)
  {
    $directory = new \DirectoryIterator($path);
    $items = [];
    foreach ($directory as $item) {
      if (!$item->isDot()) {
        $items[] = [
          'name' => $item->getFilename(),
          'path' => $item->getPathname(),
          'type' => $item->isDir() ? 'directory' : 'file',
        ];
      }
    }

    return [
      '#theme' => 'item_list',
      '#list_type' => 'ul',
      '#items' => array_map(function ($item) {
        return [
          '#type' => 'link',
          '#title' => $item['name'],
          '#url' => \Drupal\Core\Url::fromRoute('file_editor.editor', [], [
            'query' => ['path' => $item['path']],
          ]),
        ];
      }, $items),
    ];
  }

  private function renderFile($path)
  {
    $content = file_get_contents($path);

    return [
      '#type' => 'markup',
      '#markup' => '<pre>' . htmlentities($content) . '</pre>',
    ];
  }
}
