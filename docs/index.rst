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


Richiedere una squadra specifica tramite id:

.. code-block:: javascript

    query {
      team (id: "VGVhbTox"){
        name
      }
    }


Aggiungere una squadra:

.. code-block:: javascript

  mutation{
    createTeam (input: {
      name: "Saluti e baci",
      defender: 1,
      striker: 2,
    }) {
      ok
      clientMutationId
    }
  }


Aggiornare le info di una squadra. In questo esempio usiamo ID misti, sia
del db, sia quelli di graphql:


.. code-block:: javascript

    mutation{
      updateTeam (input: {
        name: "Nuovo nome",
        striker: "UGxheWVyOjE=",
        defender: "3",
        teamId: "VGVhbTox",
      }) {
        ok
        clientMutationId
      }
    }


Eliminare una squadra:

.. code-block:: javascript

    mutation{
      deleteTeam (input:{
        teamId: "VGVhbToxMA==",
      }) {
        ok
      }
    }
