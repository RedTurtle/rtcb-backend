RTCB - RedTurtle Calcio-Balilla
-------------------------------



Esempi Query
''''''''''''

Richiedere tutte le squadre:


.. code-block:: javascript

    query {
      teams {
        edges {
          node {
            id
            name
          }
        }
      }
    }


Richiedere un elemento specifico tramite id:

.. code-block:: javascript

    query {
      team (id: "VGVhbTox"){
        name
      }
    }
