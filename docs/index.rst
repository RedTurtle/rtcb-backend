RTCB - RedTurtle Calcio-Balilla
-------------------------------



Esempi Query
::::::::::::


Squadre/Team
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


Aggiornare le info di una squadra:


.. code-block:: javascript

    mutation{
      updateTeam (input: {
        name: "Nuovo nome",
        teamId: "VGVhbTox",
      }) {
        ok
        clientMutationId
      }
    }
