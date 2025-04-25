def test_dummy:
    pass


# Xpath axes
# Child axes
# //div/child::input

# Parent axes
# //input/parent::div

# Ancestor
# //input/ancestor::form

# Descendant
# //form/descendant::input

# //div/preceding::input

#//div/following::select
'''
git stash
git stash push -m "<message"
git stash list
switch to another branch
revert to current branch
git stash pop ( git stash apply stash@{0}, git stash drop stash@{0} )



 master - a->b

 feature1  ->f1
             a->b->f1 rebase cleaner history
              a->f1-b> merge will maintain history

'''

# div
#   section
#      input
# for input, div is an ancestor
# or we can say input is descendent of div
#
# div
#   div
#     input
# for input div is a precedent.